import matplotlib.pyplot as plt
Classes=['little coders','scratch','intro to python','python with pygame']
student=[500,2000,400,600]

plt.title('Students enrolled in CWK')
plt.xlabel('Class Name')
plt.ylabel('Number of Students Enrolled')
plt.bar(Classes,student,color='red', label='label for legend')
plt.legend(facecolor='lightblue')

plt.barh(student,Classes,color='red',label='Label for legend')


plt.show()