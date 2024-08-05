to_do_list = []

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    to_do_list.append(task)
    except FileNotFoundError:
        pass

def save_tasks(filename="tasks.txt"):
    with open(filename, "w") as file:
        for idx, task in enumerate(to_do_list, 1):
            file.write(f"{idx}. {task}\n")

def add_task(task_list):
    task = input("Yapılacak görevi girin: ")
    task_list.append(task)
    print("Görev başarıyla eklendi.")
    save_tasks()

def delete_task(task_list):
    show_tasks(task_list)  # Görevleri göster
    try:
        task_number = int(input("Silmek istediğiniz görev numarasını girin: ")) - 1
        if 0 <= task_number < len(task_list):
            removed_task = task_list.pop(task_number)
            print(f"'{removed_task}' görevi başarıyla silindi.")
            save_tasks()
        else:
            print("Geçersiz görev numarası.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def show_tasks(task_list):
    print("Yapılacak Görevler:")
    for idx, task in enumerate(task_list, 1):
        print(f"{idx}. {task}")

def main():
    load_tasks()
    while True:
        print("\nTo-Do List Uygulaması")
        print("1. Görev Ekle")
        print("2. Görevleri Göster")
        print("3. Görev Sil")
        print("4. Çıkış")
        choice = input("Seçiminiz (1/2/3/4): ")

        if choice == "1":
            add_task(to_do_list)
        elif choice == "2":
            show_tasks(to_do_list)
        elif choice == "3":
            delete_task(to_do_list)
        elif choice == "4":
            print("Uygulamadan çıkılıyor...")
            save_tasks()
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
