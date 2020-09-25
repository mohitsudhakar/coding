
def normalizeRule(rule):
    hor, ver = False, False
    fro_ver, to_ver = rule[0], rule[2]
    fro_hor, to_hor = rule[0], rule[2]
    if 'N' in rule[1]:
        ver = True
    if 'S' in rule[1]:
        ver = True
        fro_ver, to_ver = to_ver, fro_ver
    if 'E' in rule[1]:
        hor = True
    if 'W' in rule[1]:
        hor = True
        fro_hor, to_hor = to_hor, fro_hor
    return (fro_hor, hor, to_hor), (fro_ver, ver, to_ver)

def validateDirs(rules):
    hor_dic, ver_dic = dict(), dict()
    for rule in rules:
        print(rule)
        rule = rule.split(' ')
        rule_hor, rule_ver = normalizeRule(rule)
        if rule_hor[1]:
            # do dfs in each dir to check if this can be placed on hor_dic
            node = rule_hor[2]
            while node in hor_dic:
                if hor_dic[node] == rule_hor[0]:
                    return False
                node = hor_dic[node]
            hor_dic[rule_hor[0]] = rule_hor[2]
        print('hor', hor_dic)
        if rule_ver[1]:
            # do dfs in each dir to check if this can be placed on ver_dic
            node = rule_ver[2]
            while node in ver_dic:
                if ver_dic[node] == rule_ver[0]:
                    return False
                node = ver_dic[node]
            ver_dic[rule_ver[0]] = rule_ver[2]
        print('ver', ver_dic)
    return True

if __name__ == '__main__':

    rules = [
        "A N B",
        "B NE C",
        "C SE D",
        "A W D"
    ]
    # rules = ["A NW B", "A N B"]

    print(validateDirs(rules))