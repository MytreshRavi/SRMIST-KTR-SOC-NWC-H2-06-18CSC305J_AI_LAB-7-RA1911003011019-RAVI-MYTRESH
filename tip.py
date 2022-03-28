import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

f_qual = int(input("Rate food ? [0-10] --- "))
s_qual = int(input("Waiter service ? [0-10] --- "))
a_qual = int(input("Rate the Ambience ? [0-10]---"))

quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
ambience =ctrl.Antecedent(np.arange(0, 11, 1), 'ambience')

tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

quality.automf(3)
service.automf(3)
ambience.automf(3)

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['quality'] = f_qual
tipping.input['service'] = s_qual
tipping.input['ambience'] =a_qual

tipping.compute()

print("You should Tip ", tipping.output['tip'])

