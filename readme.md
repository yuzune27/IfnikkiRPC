# IfNikkiRPC

![Discord Rich Presence](./img/rpc.PNG)

# 概要
インフィニティニキの起動を検知し、Discordのアクティビティに表示するプログラムです。<br>
現在**スタイリストID（UID）・フレンドコード（FC）の表示**に対応しています（非表示設定も可能です）。<br>
アプリケーションはタスクトレイに格納され、右クリックの Exit を押すことでプログラムを終了できます。<br>
また、動作状況はlogフォルダ先の**ログファイル**に記述されます。

# アクティビティ設定
GUIは無いため、フォルダに同梱されている**config.json**をメモ帳等のアプリで開き、直接編集してください。

## UID
スタイリストID（UID）を**数値**で入力してください。この項目ではダブルクォーテーション「`""`」は不要です。

## FriendCode
フレンドコードを**文字列**で入力してください。

## UIDVisible
UIDの表示可否を設定します。<br>
「`true`」または「`false`」で指定してください。<br>
`true`の場合は、UIDをそのまま表示します。<br>
`false`の場合、Discord上には「__****__」と表示されます。

## FCVisible
フレンドコードの表示可否を設定します。<br>
「`true`」または「`false`」で指定してください。<br>
`true`の場合は、フレンドコードをそのまま表示します。<br>
`false`の場合、Discord上には「__****__」と表示されます。

## BtnLabel
Discordアクティビティの**ボタン名**を設定します。

## BtnUrl
Discordアクティビティの**ボタンURL**を設定します。

## （削除済み機能）
<details>
<summary>Resource(~v1.1.0)</summary>

インストール先フォルダのファイルからUIDを自動検出する手法を取っています。<br>
インフィニティニキのゲームリソースが保存されているフォルダを絶対パスで指定します。<br>
ディレクトリの移動は**バックスラッシュ2つ**「`\\`」を使ってください。

</details>

## 例
```json
{
  "UID": 123456789,
  "FriendCode": "fsAaBbCc",
  "UIDVisible": true,
  "FCVisible": false,
  "BtnLabel": "公式サイト",
  "BtnUrl": "https://infinitynikki.infoldgames.com/ja/home"
}
```

<details>
<summary>~v1.1.0</summary>

```json
{
  "Resource": "D:\\Program Files\\InfinityNikki\\",
  "UIDVisible": true,
  "BtnLabel": "公式サイト",
  "BtnUrl": "https://infinitynikki.infoldgames.com/ja/home"
}
```

</details>

# アップデート方法
自動アップデート機能を搭載していないため、各自**GitHubページ**を確認してください。
https://github.com/yuzune27/IfnikkiRPC/releases

# アンインストール方法
**ifnikkiRPC.exe**を削除してください。

# 注意事項
* 自分用に作ったアプリなので、デバッグをほとんど行っておらず、<INS>動作保証はできません</INS>。
* インフィニティニキの今後のバージョンアップデートにより<INS>動作しなくなる可能性</INS>があります。

# 参考資料
- [StarRailDiscordRPC](https://github.com/Gattxxa/StarRailDiscordRPC)
- [Wuthering-Waves-RPC](https://github.com/xAkre/Wuthering-Waves-RPC)
- [Windows のタスクトレイに Python アプリを常駐させ定期的にプログラムを実行する](https://qiita.com/bassan/items/3025eeb6fd2afa03081b)
- [discord-rich-presence](https://pypi.org/project/discord-rich-presence/)
- [PyInstallerで実行ファイルにリソースを埋め込み](https://qiita.com/firedfly/items/f6de5cfb446da4b53eeb)

Thank you!