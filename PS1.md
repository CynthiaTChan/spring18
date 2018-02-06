```python
from aide_design.play import*
```

```python
kh = np.array(np.linspace(0.1,9.9,99))
# print(kh)
g = pc.gravity
Y_axis1 = kh * np.tanh(kh)
Y_axis2 = np.sqrt(np.tanh(kh) / kh)
# test = np.sin(kh)
#print(test)
#print(Y_axis1)

plt.figure()
plt.plot(kh,Y_axis1, 'c-')
plt.xlabel('kh')
plt.ylabel('sigma^2*h*g^-1')
plt.grid
plt.show()

plt.figure()
plt.plot(kh,Y_axis2, 'r-')
plt.xlabel('kh')
plt.ylabel('cp/(gh)^.5')
plt.grid
plt.show()






```
