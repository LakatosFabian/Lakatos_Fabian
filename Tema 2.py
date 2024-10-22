articol = "Meteorologii au emis joi o avertizare cod galben de vânt puternic, pentru județul Caraș-Severin, valabilă de joi seară până duminică dimineață."

jumatate = len(articol) // 2

prima_jumatate = articol[:jumatate]
a_doua_jumatate = articol[jumatate:]

prima_jumatate = prima_jumatate.upper()
prima_jumatate = prima_jumatate.replace(" ", "")

a_doua_jumatate = a_doua_jumatate[::-1]
a_doua_jumatate = a_doua_jumatate.replace(".", "")
a_doua_jumatate = a_doua_jumatate.replace(",", "")
a_doua_jumatate = a_doua_jumatate.capitalize()

articol = prima_jumatate + a_doua_jumatate

print(prima_jumatate, a_doua_jumatate)