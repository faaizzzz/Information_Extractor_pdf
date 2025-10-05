#!/usr/bin/env python3
"""
Interactive QA System for Multiple PDFs (Colab-Ready)
Auto-detects PDF, retrieves best chunks, and summarizes.
"""

import argparse
from indexer import index_pdfs, save_index, load_index, answer_query, auto_detect_doc


def main(index_folder="pdfs"):
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=str, default=index_folder)
    parser.add_argument("--save-index", type=str, default="index.pkl")
    parser.add_argument("--load-index", type=str, default="index.pkl")
    parser.add_argument("--query", type=str, help="Ask one question directly")
    parser.add_argument("--topk", type=int, default=2)
    args, _ = parser.parse_known_args()

    # Load or build index
    try:
        index = load_index(args.load_index)
        print("✅ Index loaded successfully.")
    except:
        print(f"📂 Indexing PDFs in: {args.index}")
        index = index_pdfs(args.index)
        save_index(index, args.save_index)
        print(f"💾 Index saved to {args.save_index}")

    # Direct single query mode
    if args.query:
        chosen_doc = auto_detect_doc(args.query)
        if chosen_doc:
            print(f"\n📘 Auto-detected document: {chosen_doc}\n")
        else:
            print("\n📘 Searching across all PDFs...\n")

        results = answer_query(index, args.query, top_k=args.topk)
        if not results:
            print("❌ No relevant answer found.")
            return

        for i, (score, text, meta) in enumerate(results, 1):
            print(f"[{i}] 🔎 From {meta['source']} (score={score:.4f}):\n{text}\n")
        return

    # Interactive QA session
    print("\n💬 QA Mode started. Press ENTER on an empty line to exit.\n")
    while True:
        q = input("❓ Question: ").strip()
        if not q:
            print("👋 Exiting QA mode.")
            break

        chosen_doc = auto_detect_doc(q)
        if chosen_doc:
            print(f"\n📘 Auto-detected document: {chosen_doc}\n")
        else:
            print("\n📘 Searching across all PDFs...\n")

        results = answer_query(index, q, top_k=args.topk)
        if not results:
            print("❌ No relevant answer found.\n")
            continue

        for i, (score, text, meta) in enumerate(results, 1):
            print(f"[{i}] 🔎 From {meta['source']} (score={score:.4f}):\n{text}\n")


if __name__ == "__main__":
    main()
