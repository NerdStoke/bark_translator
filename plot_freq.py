import matplotlib.pyplot as plt
import pickle



for i in range(10,51):
    i=i*10
    data = pickle.load(open('data/data'+str(i)+'.pkl', 'rb'))
    bg = pickle.load(open('bg/bg'+str(i)+'.pkl', 'rb'))
    # print(len(data))
    # print(len(bg))
    # print(type(data))

    x = range(len(data))

    plt.plot(x,data)
    plt.plot(x,bg)
    plt.plot(x,data-bg)
    plt.show()