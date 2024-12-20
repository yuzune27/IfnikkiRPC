# IfNikkiRPC

![Discord Rich Presence](./img/rpc_new.PNG)

English Document (→[readme_en.md](./others/readme_en.md))

# 概要
インフィニティニキの起動を検知し、Discordのアクティビティに表示するプログラムです。<br>
現在**スタイリストID（UID）・フレンドコード（FC）の表示**に対応しています（非表示設定も可能です）。<br>
アプリケーションはタスクトレイに格納され、右クリックの Exit を押すことでプログラムを終了できます。<br>
また、動作状況はlogフォルダ先の**ログファイル**に記述されます。

# アクティビティ設定
GUIは無いため、フォルダに同梱されている**config.json**をメモ帳等のアプリで開き、直接編集してください。

## Lang
言語を**文字列**で設定します。設定した言語はゲームタイトルに反映されます。<br>

### 対応言語
|     言語      |  値   |
|:-----------:|:----:|
|   **日本語**   |  ja  |
| **English** |  en  |

<INS>この設定を変更した場合、アプリの再起動が必要です。</INS>

## Player
プレイヤー名を**文字列**で設定します。<br>
PCの場合、アクティビティの**小アイコン**にマウスを合わせると表示されます。

## UID
スタイリストID（UID）を**数値**で入力してください。この項目ではダブルクォーテーション「`""`」は不要です。

## FriendCode
フレンドコードを**文字列**で入力してください。
<details>
<summary>Tip</summary>
インフィニティニキのフレンドコードは1つにつき1人しか使えない仕様です。<br>
一方でもし複数人募集したい場合、全てのフレンドコードを全文字記載すると煩雑になりがちですよね（場合によっては文字数制限でプログラムエラーになる可能性も）。<br>
そこで次のような省略記法で記述することで枠を圧迫せずに済みます。

```text
"fsAaBb** AB/Ah/kd/k2"
"fsAaBbC* S/a/3/h/H"
```

これはフレンドコードを短期間で一気に発行した時、文字列の**最後の1～2文字以外が固定される**ことを利用しています（要検証）。<br>
「__*__（__**__）」の部分は右のスラッシュで区切られた部分の文字列を当てはめれば良いわけです。<br>

（あくまで提案なので必ずしもこの記述を強制するものではありません。）
</details>


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
  "Lang": "ja",
  "Player": "Name",
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
**タスクトレイにあるアプリ**を**右クリック**することでアップデートの有無が確認できます（v1.4.0以降）。<br>
アップデートが利用可能な場合、メニューをクリックするとブラウザでダウンロードページを開きます。<br>
![Update Image](./img/update_check.PNG)

# アンインストール方法
ifnikkiRPCのフォルダを削除してください。

# 注意事項
* ボタンURLに**有害なサイト**を貼らないでください。
* インフィニティニキの今後のバージョンアップデートにより<INS>動作しなくなる可能性</INS>があります。

# 参考資料
- [StarRailDiscordRPC](https://github.com/Gattxxa/StarRailDiscordRPC)
- [Wuthering-Waves-RPC](https://github.com/xAkre/Wuthering-Waves-RPC)
- [Windows のタスクトレイに Python アプリを常駐させ定期的にプログラムを実行する](https://qiita.com/bassan/items/3025eeb6fd2afa03081b)
- [discord-rich-presence](https://pypi.org/project/discord-rich-presence/)
- [PyInstallerで実行ファイルにリソースを埋め込み](https://qiita.com/firedfly/items/f6de5cfb446da4b53eeb)

Thank you!