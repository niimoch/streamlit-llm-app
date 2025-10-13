# # app.py
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 1 タイトル
st.title("LLM機能を搭載したWebアプリ")

# 2 環境変数の読み込み
load_dotenv()

# 3 LLM初期化（1回だけ）
if "llm" not in st.session_state:
    st.session_state.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm = st.session_state.llm

# 4 専門家モードの選択
mode = st.radio(
    "話を聞いてくれる人を選んでね：",
    options=[
        "A：ITにちょっと詳しいお兄さん",
        "B：ポジティブ思考のコーチ",
    ],
    index=0,
    horizontal=True,
)

# 5 選択値に応じたSystemメッセージ
expert_prompts = {
    "A：ITにちょっと詳しいお兄さん": (
        "あなたは優しいITに詳しいお兄さん。難しい専門用語を避けて、"
        "中学生にも分かるように具体例を交えながら説明してね。"
        "答えは簡潔で、語尾はやわらかく。"
    ),
    "B：ポジティブ思考のコーチ": (
        "あなたはポジティブ思考を教えるコーチ。"
        "相手を励ましながら、前向きな考え方を提案してあげて。"
        "否定的な言葉は使わず、温かい言葉を中心に答えること。"
    ),
}

# 6 入力フォーム
user_text = st.text_input("質問（1行）を入力してね：", placeholder="例）やる気が出ない時はどうすればいい？")


# 7 関数定義（←課題のメインポイント）
def get_llm_response(text: str, mode: str) -> str:
    """入力テキストと選択モードを受け取り、LLMの回答を返す"""
    system_text = expert_prompts[mode]
    messages = [
        SystemMessage(content=system_text),
        HumanMessage(content=text),
    ]
    result = llm(messages)
    return result.content


# 8 実行と表示
if st.button("送信") and user_text.strip():
    answer = get_llm_response(user_text, mode)
    st.subheader(f"応答（{mode}モード）")
    st.write(answer)

