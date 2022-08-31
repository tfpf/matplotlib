import matplotlib.pyplot as plt

plt.rc('mathtext', fontset='cm') # size=30; num1 = 0.8; num2 = 0.9; num3 = 0.8; denom1 = 0.9; denom2 = 0.7
plt.rc('mathtext', fontset='stix') # size=30; num1 = 1.6; num2 = 1.6; num3 = 1.6; denom1 = 1.6; denom2 = 1.1
plt.rc('mathtext', fontset='stixsans') # size=30; num1 = 1.5; num2 = 1.5; num3 = 1.5; denom1 = 1.5; denom2 = 1.1
plt.rc('mathtext', fontset='dejavuserif') # size=30; num1 = 1.5; num2 = 1.6; num3 = 1.4; denom1 = 1.4; denom2 = 1.1
plt.rc('mathtext', fontset='dejavusans') # size=30; num1 = 1.4; num2 = 1.5; num3 = 1.3; denom1 = 1.3; denom2 = 1.1
plt.rc('mathtext', fontset='custom') # size=30; num1 = 1.7; num2 = 1.8; num3 = 1.7; denom1 = 1.6; denom2 = 1.2

for fontset in ('cm', 'stix', 'stixsans', 'dejavuserif', 'dejavusans', 'custom')[-1 :]:
    plt.rc('mathtext', fontset=fontset)
    fig = plt.figure()
    fig.canvas.manager.window.maximize()
    fig.text(0, 0.80, r'$-\dfrac{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}$', size=30)
    fig.text(0, 0.70, r'$-\frac{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}$', size=30)
    fig.text(0, 0.50, r'$-\genfrac{}{}{0}{0}{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}$', size=30)
    fig.text(0, 0.40, r'$-\genfrac{}{}{0}{1}{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}$', size=30)
    # fig.text(0, 0.30, r'$-\genfrac{}{}{0}{2}{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}$', size=30)
    # fig.text(0, 0.20, r'$-\genfrac{}{}{0}{3}{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}{0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}$', size=30)
plt.show()
