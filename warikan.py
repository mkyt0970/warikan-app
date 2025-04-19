def calculate_split():
    print("割り勘アプリへようこそ！")

    # 人数と情報の入力
    num_people = int(input("参加人数を入力してください: "))
    names = []
    payments = []
    
    for i in range(num_people):
        name = input(f"{i+1}人目の名前を入力してください: ")
        amount = float(input(f"{name}さんが支払った金額を入力してください: "))
        names.append(name)
        payments.append(amount)

    # 平均額を計算
    total = sum(payments)
    average = total / num_people
    diffs = [round(payment - average, 2) for payment in payments]

    print("\n--- 精算結果 ---")
    for i in range(num_people):
        if diffs[i] > 0:
            print(f"{names[i]}さんは {diffs[i]:.2f}円 多く払っています。")
        elif diffs[i] < 0:
            print(f"{names[i]}さんは {-diffs[i]:.2f}円 少なく払っています。")
        else:
            print(f"{names[i]}さんは ちょうどの金額を払っています。")

    # 「誰が誰にいくら払えばいいか」の計算
    print("\n--- 支払い提案 ---")
    debtors = []
    creditors = []

    for i in range(num_people):
        if diffs[i] < 0:
            debtors.append({"name": names[i], "amount": -diffs[i]})
        elif diffs[i] > 0:
            creditors.append({"name": names[i], "amount": diffs[i]})

    # 精算ループ
    i = 0
    j = 0
    while i < len(debtors) and j < len(creditors):
        debtor = debtors[i]
        creditor = creditors[j]
        pay_amount = min(debtor["amount"], creditor["amount"])
        
        print(f"{debtor['name']}さん → {creditor['name']}さんに {pay_amount:.2f}円 払う")

        debtor["amount"] -= pay_amount
        creditor["amount"] -= pay_amount

        if debtor["amount"] == 0:
            i += 1
        if creditor["amount"] == 0:
            j += 1

# 実行
calculate_split()