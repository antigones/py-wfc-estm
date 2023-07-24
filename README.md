# py-wfc-estm
"Even Simpler Tile Model", like explained in:

https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/

Sample usage:

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
    emoji_map = {'L':'🌴','C':'⛱️ ','S':'🌊','K':'🏄','B':'⛵'}
    emoji_print(sol,emoji_map)

Output:

    🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴
    ⛱️🌴🌴🌴🌴🌴🌴🌴🌴🌴
    🌊⛱️🌴⛱️🌴🌴🌴🌴🌴🌴
    ⛵🌊⛱️🌊⛱️🌴⛱️🌴🌴🌴
    🌊🏄🌊🌊🌊⛱️🌊⛱️🌴🌴
    ⛵🌊🏄🌊🌊🌊🌊🌊⛱️🌴
    🌊⛵🌊🏄🌊🌊🌊⛵🌊⛱️
    🌊🌊🌊🌊🌊🏄🌊🌊🌊🌊
    🌊🏄🌊⛵🌊🌊🌊⛵🌊🌊
    🌊🌊🏄🌊⛵🌊🌊🌊🌊⛵

