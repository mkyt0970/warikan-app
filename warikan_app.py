import streamlit as st

st.title("時代は割り勘🍺")
st.write("みんなの支払額を入力して、誰が誰にいくら払えばいいかを計算します。")

num_people = st.number_input("参加人数を入力", min_value=2, step=1)

if num_people:
    names = []
    payments = []
    
    for i in range(num_people):
        name = st.text_input(f"{i+1}人目の名前", key=f"name_{i}")
        amount = st.number_input(f"{name or f'参加者{i+1}'}さんの支払額", key=f"amount_{i}")
        names.append(name if name else f"参加者{i+1}")
        payments.append(amount)
    
    if st.button("割り勘する！"):
        total = sum(payments)
        average = total / num_people
        diffs = [round(p - average, 2) for p in payments]

        st.subheader("📊 精算結果")
        for i in range(num_people):
            diff = diffs[i]
            if diff > 0:
                st.write(f"{names[i]} さんは **{diff:.2f}円多く**払っています。")
            elif diff < 0:
                st.write(f"{names[i]} さんは **{-diff:.2f}円少なく**払っています。")
            else:
                st.write(f"{names[i]} さんは **ちょうど**払っています。")

        st.subheader("💸 支払い提案")
        debtors = []
        creditors = []
        for i in range(num_people):
            if diffs[i] < 0:
                debtors.append({"name": names[i], "amount": -diffs[i]})
            elif diffs[i] > 0:
                creditors.append({"name": names[i], "amount": diffs[i]})

        i = 0
        j = 0
        while i < len(debtors) and j < len(creditors):
            debtor = debtors[i]
            creditor = creditors[j]
            pay_amount = min(debtor["amount"], creditor["amount"])
            st.write(f"{debtor['name']} → {creditor['name']} に **{pay_amount:.2f}円払う**")

            debtor["amount"] -= pay_amount
            creditor["amount"] -= pay_amount

            if debtor["amount"] == 0:
                i += 1
            if creditor["amount"] == 0:
                j += 1