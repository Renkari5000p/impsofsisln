#!/usr/bin/env python
# coding: utf-8

# In[21]:


mi_captura = input('Escribe algo aqui:   ')
try:
    if (int == type(mi_capktura )):
     print("tipo correcto string")
    else:
        print("ingresa el numero correcto")
except: 
    print("ocurrio un error")


# In[29]:


mi_captura2 = int(input('escribe tu edad:   '))
try:
    print(mi_captura2.CONVERT)
except:
    print("print manejar error")

if'carlos' == carlos.nombre:
    print("eres carlos")
except NameError:
    print("define la variable carlos primero")


# In[37]:


edad = int(input('escribe tu edad:   '))
try:
    print(edad+2)
except TypeError:
    print(int(edad)+2)

try:
    if'carlos' == carlos.nombre:
       print("eres carlos")
except NameError:
    print("define la variable carlos primero")


# In[57]:


except NameError:
    print("define la variable carlos primero")
try:
    print("busca el error")
except SyntaxError:
    print("esta mal")


# In[60]:


print(i)


# In[68]:


#calcular en base a un valor dado por el usuario
#su equivalencia en las diferentes divisas definidas

#china
yuan=2.81
#japon
yen=0.13
#estados_unidos
dolar=20.54
#union_europea
euro=21.29
#reino_unido
libras=25.57

pesos=input("ingresa la cantidad de pesos a convertir")
pesos=int(pesos)
print("los pesos equivalen a ")
print("tus pesos son %2f yuanes" %(pesos/yuan))
print("tus pesos son %2f yenes" %(pesos/yen))
print("tus pesos son %2f dolares" %(pesos/dolar))
print("tus pesos son f euros" %(pesos/euro))
print("tus pesos son %2f libras" %(pesos/libras))


# In[70]:


numero = int(input("numero para ver si es par o inpar"))
if numero % 2 == 0:
    print("el numero es par")
else:
print ("el numro es inpar")


# In[74]:


dia = int(input("escribe el numero de dia"))
=["lunes","martes" ,"miescoles" ,"jueves" ,"viernes" ,"sabado" ,"domingo"]
print("el dia de la semana es",dias_de_la_semana[dia-1])


# In[97]:


a = 4; b = 0
print(a/b)


# In[103]:


a = 5
b = 0
# A través de esta comprobación prevenimos que se divida entre cero.
if b!=0:
    print(a/b)
else:
    print("No se puede dividir!")


# In[105]:


raise ZeroDivisionError("Información de la excepción")


# In[107]:


raise ZeroDivisionErrorraise ZeroDivisionError


# In[109]:


try:
    # Forzamos una excepción al dividir entre 0
    x = 2/0
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")


# In[113]:


try:
    # Forzamos excepción
    x = 2/0
except:
    # Se entra ya que ha habido una excepción
    print("Entra en except, ha ocurrido una excepción")
finally:
    # También entra porque finally es ejecutado siempre
    print("Entra en finally, se ejecuta el bloque finally")

#Entra en except, ha ocurrido una excepción
#Entra en finally, se ejecuta el bloque finally


# In[117]:


try:
    with open('fichero.txt') as file:
        read_data = file.read()


# In[125]:


while True:
 


# In[127]:


for arg in sys.argv[1:]:


# In[133]:


try:
    open("database.sqlite")


# In[139]:


def func:
    raise ConnectionError


# In[ ]:




