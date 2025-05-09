import streamlit as st
from datetime import datetime

st.title("📅 ToDoリスト")

#初期化
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

#タスク追加
with st.form("add_task"):
    task = st.text_input("タスク内容")
    deadline = st.date_input("期限",value=datetime.today())
    priority = st.selectbox("優先度",["高","中","小"])
    progress = st.slider("進捗(%)",0,100,0)
    submitted = st.form_submit_button('追加')

if submitted and task:
    st.session_state.tasks.append({
        "内容": task,
        "期限": deadline.strftime('%Y-%m-%d'),
        "優先度": priority,
        "進捗": progress
     })

#表示とフィルター
filter_option = st.selectbox("表示フィルター",["全て","未完了のみ"])

for i, t in enumerate(st.session_state.tasks):
    if filter_option == "未完了のみ" and t["進捗"] == 100:
        continue

    st.write(f"**{t['内容']}**")
    st.write(f"📅 締切:{t['期限']}｜🎯 優先度:{t['優先度']}|📈 進捗:{t['進捗']}%")

    col1, col2 = st.columns(2)
    if col1.button(f"☑️ 完了({i})"):
        st.session_state.tasks[i]["進捗"] = 100
    if col2.button(f"🗑️ 削除({i})"):
        st.session_state.tasks.pop(i)
        st.rerun()