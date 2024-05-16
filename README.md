
Streamlit RAG 実装チュートリアル 
はじめに 

このリポジトリは、Streamlit を使用して Retrieval-Augmented Generation (RAG) モデルを実装するためのチュートリアルです。 RAG モデルは、AI を活用して検索と回答を行うことができ、大量のデータを効率的に扱うことができます。

必要なライブラリ
streamlit
dotenv
llama-index
openai

使い方

ライブラリのインストール 
このリポジトリをクローンした後、以下のコマンドを実行して必要なライブラリをインストールしてください。
pip install -r requirements.txt

API KEY の設定
.env で自分んのKEY に設定

プログラムの実行 
streamlit run app.py

内容 

app.py - Streamlit アプリケーションのメインスクリプトです。
requirements.txt - 実行に必要なライブラリのリストです。
.env
data

注意 
このチュートリアルは、RAG モデルの基本的な実装を紹介しています。実際の用途に合わせてカスタマイズしてください。
ライブラリのバージョンによっては、エラーが発生する場合があるため、必要に応じてバージョンを調整してください。
