import time, random

# 展示角色属性
player_life = 100
player_attack = 35
enemy_life = 105
enemy_attack = 33


# 显示角色属性函数
def show_role(player_life, player_track, enemy_life, enemy_track):
    print('【玩家】\n血量:%d\n攻击:%d' % (player_life, player_track))
    print('----------------------------')
    time.sleep(1.5)

    print('【敌人】\n血量:%d\n攻击:%d' % (enemy_life, enemy_attack))
    print('----------------------------')
    time.sleep(1.5)


# 双方PK函数代码
def pk_role(player_life, player_track, enemy_life, enemy_track):
    while (player_life > 0) and (enemy_life > 0):
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack

        print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))  # 人工计算敌人血量
        print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))  # 人工计算玩家血量
        print('----------------------------')
        time.sleep(1.5)
    show_result(player_life, enemy_life)


# 打印战果
def show_result(player_life, enemy_life):
    if player_life > 0 and enemy_life <= 0:
        print('敌人死翘翘了，这局你赢了')
    elif player_life <= 0 and enemy_life > 0:
        print('悲催，这局敌人把你干掉了！')
    else:
        print('哎呀，这局你和敌人同归于尽了！')
    print('-----------------------')


# 定义一个主函数
def main(player_life, player_track, enemy_life, enemy_track):
    show_role(player_life, player_track, enemy_life, enemy_track)
    pk_role(player_life, player_track, enemy_life, enemy_track)


main(100, 35, 105, 33)
