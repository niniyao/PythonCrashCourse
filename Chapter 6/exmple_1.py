alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#加items，里面的key-value pair不分顺序
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#modifying values in a dictionary
alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + ".")

alien_0 = {
    'color': 'green',
    'points': 5,
    'x_position': 0,
    'y_position': 25,
    }
# 最后一个逗号可有可无，如果确定还要添加，最好就写上