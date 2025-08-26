l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
s = l * a
t = s / 2
print('Sua tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, s))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(t))