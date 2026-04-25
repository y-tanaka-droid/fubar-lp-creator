#!/usr/bin/env python3
"""
LP制作くん — CLIスクリプト版
使い方: python3 scripts/generate_lp.py --client "クライアント名" --industry "業種"
"""

import argparse
import os
import re
import sys
from pathlib import Path
from datetime import datetime

TEMPLATES_DIR = Path(__file__).parent.parent / "templates"
OUTPUT_DIR = Path(__file__).parent.parent / "output"


def load_template(template_name: str) -> str:
    path = TEMPLATES_DIR / template_name
    if not path.exists():
        print(f"❌ テンプレートが見つかりません: {path}")
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def fill_template(html: str, variables: dict) -> str:
    for key, value in variables.items():
        html = html.replace("{{" + key + "}}", value)
    return html


def save_output(client_name: str, html: str) -> Path:
    safe_name = re.sub(r'[^\w\-]', '_', client_name)
    out_dir = OUTPUT_DIR / safe_name
    out_dir.mkdir(parents=True, exist_ok=True)

    index_path = out_dir / "index.html"
    index_path.write_text(html, encoding="utf-8")

    # README自動生成
    readme = f"""# {client_name} LP

## 作成日
{datetime.now().strftime('%Y-%m-%d')}

## 公開URL
（デプロイ後に記入）

## LINE URL
（要記入）

## 修正メモ
- [ ] SP表示確認
- [ ] LINE URL差し替え
- [ ] OGP画像設定
"""
    (out_dir / "README.md").write_text(readme, encoding="utf-8")
    return index_path


def interactive_fill(html: str) -> str:
    """未埋めの変数をインタラクティブに入力させる"""
    remaining = re.findall(r'\{\{(\w+)\}\}', html)
    remaining = list(dict.fromkeys(remaining))  # 重複除去

    if not remaining:
        return html

    print(f"\n📝 未設定の項目が {len(remaining)} 件あります。順番に入力してください。")
    print("   （スキップする場合はEnterを押してください）\n")

    for var in remaining:
        val = input(f"  {var}: ").strip()
        if val:
            html = html.replace("{{" + var + "}}", val)

    return html


def main():
    parser = argparse.ArgumentParser(description="LP制作くん — LP自動生成スクリプト")
    parser.add_argument("--client", required=True, help="クライアント名")
    parser.add_argument("--industry", default="", help="業種")
    parser.add_argument("--line-url", default="https://line.me/R/ti/p/XXXXX", help="LINE友だち追加URL")
    parser.add_argument("--template", default="fubar_brand_lp.html", help="使用テンプレート")
    parser.add_argument("--main-color", default="#1a2f5a", help="メインカラー")
    parser.add_argument("--accent-color", default="#d4af37", help="アクセントカラー")
    parser.add_argument("--interactive", action="store_true", help="残り変数をインタラクティブに入力")
    args = parser.parse_args()

    print(f"\n🚀 LP制作くん起動")
    print(f"   クライアント: {args.client}")
    print(f"   テンプレート: {args.template}\n")

    html = load_template(args.template)

    # 基本変数を埋める
    basic_vars = {
        "MAIN_COLOR": args.main_color,
        "ACCENT_COLOR": args.accent_color,
        "LINE_URL": args.line_url,
        "PAGE_TITLE": f"{args.client} | FUBAR",
        "META_DESCRIPTION": f"{args.client}の公式LP。{args.industry}に特化したサービスです。",
        "OGP_TITLE": args.client,
        "OGP_DESCRIPTION": f"{args.client}の公式LP",
        "OGP_IMAGE_URL": "https://fubar.co.jp/ogp.jpg",
        "COMPANY_NAME": args.client,
    }
    html = fill_template(html, basic_vars)

    if args.interactive:
        html = interactive_fill(html)

    out_path = save_output(args.client, html)
    print(f"✅ 生成完了: {out_path}")
    print(f"   ブラウザで確認: open {out_path}")

    # ブラウザで開く
    os.system(f"open '{out_path}'")


if __name__ == "__main__":
    main()
