cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print$2, $1}'

# 文件 类似 ‘the day i like i go to school the day is good i like you’
