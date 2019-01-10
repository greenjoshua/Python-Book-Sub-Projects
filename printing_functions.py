from printing_models import print_models as pm
from printing_models import show_completed_models as scm

unprinted_designs = ['lg stylo case' , 'polycarbonate' , 'steel armor']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)