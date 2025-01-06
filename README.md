## Условие
Для данной функции $z(x,y) = (x^2 - xy + 2y^2)\exp(x + 2y)$ найти точки локальных экстремумов.
## Решение
### Аналитический этап
#### Стационарные точки
$$z'_x = (2x - y)\exp(x + 2y) + (x^2 - xy + 2y^2)\exp(x + 2y) = (x^2 -xy + 2y^2+ 2x - y)\exp(x + 2y)$$
$$z'_y = (4y - x)\exp(x + 2y) + 2(x^2 - xy + 2y^2)\exp(x + 2y) = (2x^2 - 2xy + 4y^2 + 4y - x)\exp(x + 2y)$$
$$\begin{cases}z'_x = 0 \\ z'_y = 0\end{cases} \Rightarrow \begin{cases}x^2 - xy + 2y^2 + 2x - y = 0 \\ 2x^2 - 2xy + 4y^2 + 4y - x = 0\end{cases}\Rightarrow 4x - 4y -2y + x = 0 \Rightarrow 5x = 6y \Rightarrow y = \frac56 x$$
$$x^2 - \frac56x^2 + \frac{25}{18}x^2 + 2x - \frac56x = 0 \Rightarrow \frac{28}{18}x^2 + \frac76 x = 0 \Rightarrow x(4x + 3) = 0$$
Имеем две стационарные точки.
$$M_0\left(-\frac34;-\frac58\right),\quad M_1(0,0).$$
#### Достаточное условие экстремума
$$\begin{gather}
z''_{xx} = (2x - y + 2)\exp(x + 2y) + (x^2 - xy + 2y^2 + 2x - y)\exp(x+2y) = \\ = (x^2 -xy + 2y^2 + 4x - 2y + 2)\exp(x + 2y) \\
z''_{yy} = (8y - 2x + 4)\exp(x + 2y) + 2(2x^2 - 2xy + 4y^2 + 4y - x)\exp(x + 2y) =\\= (4x^2 - 4xy + 8y^2 + 16y - 4x + 4)\exp(x + 2y) \\
z''_{xy} = (4y -x - 1)\exp(x + 2y) + 2(x^2 - xy + 2y^2 + 2x -y)\exp(x + 2y) = \\ = (2x^2 - 2xy + 4y^2 + 3x + 2y - 1)\exp(x+2y) 
\end{gather}
$$
Проверим достаточное условие экстремума.
$$H_z(M_1) = \begin{pmatrix}2 & -1 \\ -1 & 4\end{pmatrix}$$
$$\Delta_1 = 2 > 0,\quad \Delta_2 = 8 - 1 = 9 > 0$$
Значит, $M_1$ - это точка минимума.
$$H_z(M_0) = \begin{pmatrix}\frac{9}{8e^2} & -\frac{11}{4e^2}\\-\frac{11}{4e^2} & \frac{1}{2e^2}  \end{pmatrix}$$
$$\Delta_1 = \frac{9}{8e^2} > 0,\quad \Delta_2 = \frac{1}{2e^2}\left(\frac94 - \frac{121}{4}\right) = -14e^{-2} < 0$$
Тем самым, в точке $M_0$ нет экстремума.