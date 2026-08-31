print("hvor mange er dere på laget?")
lag_kamerater = int(input())
print("Hvor mange twist er det i posen dere vant?")
Antall_twist = int(input())
twist = Antall_twist//lag_kamerater
til_overs = Antall_twist%lag_kamerater
print(f"Det blir {twist} twist til hver, og det blir {til_overs} twist til overs.")