#!/usr/bin/env python3
"""Discord QR code generator bot"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Discord QR code generator bot")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("qr-bot v0.1.0");return
 print(f"[12:13] qr-bot ready")
if __name__=="__main__":main()
