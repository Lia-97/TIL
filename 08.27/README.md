## TIL(08.27) 

### 파이썬으로 JSON 다루기

```python
import json
json_str = '[{"name":"jihye", "age":"25"}]'
json_obj = json.loads(json_str)

print(json_obj)
```

결과

```python
[{"name":"jihye", "age":"25"}]
```

- 첫번째 줄에 import  json을 이용해 json이라는 패키지를 불러온다. 이 패키지는 json형태의 데이터를 파이썬에서 사용할 수 있도록 해준다.

- json.loads()를 이용해 JSON 형태로 되어있는 text를 json 오브젝트로 만들어 줄 수 있다. 여기에서 오브젝트는 파이썬에서 다룰 수 있는 형태라고 생각.
  - 파이썬에서 다룰 수 있는 형태? 인덱스를 이용해 접근하거나, key로 접근할 수 있음



```python
import json
json_str = '[{"name":"jihye", "age":"25"}]'
json_obj = json.loads(json_str)

print(json_obj)
print(json_obj[0])
```

결과

```python
[{"name":"jihye", "age":"25"}]
{"name":"jihye", "age":"25"}
```

- json_obj[0]을 사용해 json_obj에 들어 있는 항목 중 첫번째 항목을 선택



```python
import json
json_str = '[{"name":"jihye", "age":"25"},{"name":"sumi", "age":"28"}]'
json_obj = json.loads(json_str)

print(json_obj)
print(json_obj[0:2])
print(json_obj[0]['name'])
print(json_obj[0]['age'])
```

결과

```python
[{"name":"jihye", "age":"25"}]
[{"name":"jihye", "age":"25"},{"name":"sumi", "age":"28"}]
jihye
25
```



#### 반복문을 이용해서 데이터 출력

```python
import json
json_str = '[{"name":"jihye", "age":"25"},{"name":"sumi", "age":"28"}]'
json_obj = json.loads(json_str)

for student in json_obj:
	print(student)
   
for student in json_obj:
    print(student['name'])
    
for student in json_obj:
    print(student['name']['age'])
    
for student in json_obj:
    print(sutdent['name']+','+student['age'])
```

결과

```
{"name":"jihye", "age":"25"}
{"name":"jihye", "age":"25"}

jihye
sumi

jihye 25
sumi 28

jihye, 25
sumi, 28
```

- 가장 아래와 같이 출력하면, 특정 기호를 이용해 엑셀에서 데이터 나누기 기능을 사용할 수 있음.