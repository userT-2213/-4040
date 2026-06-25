import streamlit as st
from PIL import Image
import os

# 画面のタイトルとレイアウトの設定
st.set_page_config(page_title="授業問題復習アプリ", layout="centered")
st.title("📚 授業問題復習アプリ")
st.caption("現在の状態：資料アップロード画面（未生成）")

st.markdown("""
### 📄 ステップ1: 資料・教科書画像のアップロード
まずは復習問題の元となる、講義資料や教科書の画像をアップロードしてください。
""")

# 1. ユーザー入力の検証（対応拡張子の制限）を含んだアップロード機能
uploaded_file = st.file_uploader(
    label="資料の画像ファイルを選択してください (対応形式: PNG, JPG, JPEG)",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=False
)

# 2. ファイルがアップロードされた場合の処理
if uploaded_file is not None:
    try:
        # 画像ファイルとして正しく読み込めるか検証（破損チェックを兼ねたエラーハンドリング）
        image = Image.open(uploaded_file)
        
        # 成功時のメッセージ表示
        st.success("✅ 資料のアップロードに成功しました！")
        
        # アップロードされた画像の表示（完了条件）
        st.subheader("🖼 アップロードされた資料の確認")
        st.image(image, caption=f"ファイル名: {uploaded_file.name}", use_container_width=True)
        
        st.info("💡 完了条件達成：画像の表示を確認できました。次のステップでは、この資料を基にした問題生成ロジックを実装します。")
        
    except Exception as e:
        # 拡張子が偽装されている場合や、ファイルが破損している場合のエラー表示
        st.error(f"❌ 画像ファイルの読み込みに失敗しました。ファイルが破損しているか、正しい画像フォーマットではない可能性があります。エラー詳細: {e}")
else:
    # ファイルが未選択の場合の初期警告表示
    st.warning("⚠️ まだ資料がアップロードされていません。画像をドラッグ＆ドロップするか、ブラウズから選択してください。")