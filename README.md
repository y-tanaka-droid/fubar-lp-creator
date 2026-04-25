# 🚀 LP制作くん — FUBAR LP Generator

> FUBAR社内向けLP制作AIツール。クライアント名と業種を伝えるだけで、HTML納品ファイルまで自動生成します。

---

## 使い方（3ステップ）

### Step 1: このリポジトリをクローン
```bash
git clone https://github.com/yukis9932-maker/fubar-lp-creator.git
cd fubar-lp-creator
```

### Step 2: Claude Codeを起動
```bash
claude
```

### Step 3: LP制作を依頼する
```
/lp-create
```

あとはClaude（LP制作くん）が質問してくれます。答えるだけでLPが完成します。

---

## 依頼例

```
/lp-create

クライアント: 株式会社〇〇
業種: ジム・パーソナルトレーニング
ターゲット: 30〜40代のダイエットしたいビジネスマン
強み: 完全個室・管理栄養士監修・3ヶ月で平均-8kg実績
LINE URL: https://line.me/R/ti/p/XXXX
```

---

## 出力されるもの

```
output/
  [クライアント名]/
    index.html    ← そのままFTPでアップできる納品ファイル
    README.md     ← URL・LINE URL・修正メモ
```

---

## ファイル構成

```
fubar-lp-creator/
  CLAUDE.md                        ← LP制作くんの頭脳（読まないで）
  README.md                        ← この説明書
  .claude/
    settings.json                  ← 許可設定
    skills/lp-create/SKILL.md     ← /lp-create スキル
  docs/
    LP制作くん_総合ナレッジベース.md  ← LP制作の全ノウハウ
  templates/
    base_lp.html                  ← 汎用テンプレート（{{変数}}形式）
    fubar_brand_lp.html           ← FUBARブランドテンプレート
  scripts/
    generate_lp.py                ← CLIで直接生成するスクリプト（上級者向け）
  output/                         ← 生成されたLPの納品ファイル置き場
  examples/                       ← 参考サンプル
```

---

## テンプレートの変数一覧

テンプレートHTMLは `{{VARIABLE_NAME}}` 形式で変数が埋め込まれています。
Claude（LP制作くん）が自動で埋めますが、手動で編集する場合は以下を参照:

| 変数 | 内容 |
|------|------|
| `{{PAGE_TITLE}}` | ページタイトル |
| `{{LINE_URL}}` | LINE友だち追加URL |
| `{{HERO_COPY_1}}` | FVキャッチコピー1行目 |
| `{{HERO_COPY_ACCENT}}` | FV強調テキスト（金色） |
| `{{MAIN_COLOR}}` | メインカラー（例: #1a2f5a） |
| `{{ACCENT_COLOR}}` | アクセントカラー（例: #d4af37） |

詳細は `templates/base_lp.html` を参照。

---

## 管理・運用ルール

- 納品ファイルは `output/[クライアント名]/` に保存
- 修正履歴は `output/[クライアント名]/README.md` に記録
- テンプレートを改善したら必ずこのリポジトリにpushすること
- ナレッジ（`docs/`）を更新したら全員に共有すること

---

## 担当・問い合わせ

- 齋藤優輝（代表）
- info@fubar.co.jp

---

*Powered by Claude Code × FUBAR Inc.*
