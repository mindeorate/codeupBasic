print('"!@#$%^&*()' + "'") #그냥 출력만 하면 된다 == 내 마음대로 해도 된다

#cf) + : 쉽게 글자를 더해준다 생각하면 됨
print("a"+"b") #ab가 출력됨

#cf2) print(a+b) : ""나 ''로 문자열이란 걸 명시 안했기 때문에 오류남

#cf3)굳이 a, b라고 쓰고 싶으면
a = '"!@#$%^&*()' #이렇게 각각 지정해주면 됨
b = "'"

print(a + b)
