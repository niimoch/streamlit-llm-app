# app.py
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage

# １ envから環境変数を読み込み
load_dotenv()

# ２ OpenAIクライアントを初期化（環境変数 OPENAI_API_KEY を自動利用）
client = OpenAI()

# ３ 画面タイトル
st.title("LLM機能を搭載したWebアプリ")

