N = 556;#int(input());


hour = N // 3600;
minutes = (N % 3600) // 60;
seconds = N % 60;


print(f"{hour}:{minutes}:{seconds}");
