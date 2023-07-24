

from colorama import just_fix_windows_console, Fore, Style
from estm.estm import ESTM

from estm.estm_rule_parser import ESTMRuleParser


just_fix_windows_console()


def pretty_print(matrix, color_map):
    out = list()
    for elm in matrix:
        contents = [tuple(x)[0] for x in elm]
        content = [color_map[x]+x for x in contents]
        out.append("".join(content))
    print('\n'.join(out))
    print(Style.RESET_ALL)


def emoji_print(matrix, emoji_map):
    out = list()
    for elm in matrix:
        contents = [tuple(x)[0] for x in elm]
        content = [emoji_map[x] for x in contents]
        out.append("".join(content))
    print('\n'.join(out))


if __name__ == "__main__":
   
    img = [
            'LLLLLLLLLL',
            'LLLLLLLLLL',
            'LLLLLLLLLL',
            'LLLLLLLLLL',
            'LLLLLCLLCC',
            'LLLLCSCCSS',
            'LLLCSSSSSS',
            'LLCSSSBSSS',
            'LCSSSSSSKS',
            'CSSSSSSSSS'
            ]
    rule_parser = ESTMRuleParser(img)
    rules, weights = rule_parser.calc_rules()

    wfc = ESTM(size=10, rules=rules, weights=weights)
    sol = wfc.solve()
    # color_map = {'L':Fore.GREEN,'C':Fore.YELLOW,'S':Fore.BLUE,'D':Fore.CYAN}
    # pretty_print(sol)
    emoji_map = {'L':'🌴','C':'⛱️ ','S':'🌊','K':'🏄','B':'⛵'}
    emoji_print(sol,emoji_map)