import b_calc as bc


m_arg1, m_arg2, m_action = bc.input_date()
try:
    m_arg1, m_arg2, m_action = bc.check_date(m_arg1, m_arg2, m_action)
except CalcException as e:
    print(e)
    exit(1)
bc.output_date(m_arg1, m_arg2, m_action)
# from b_calc import input_date
#
# a, b, c = input_date()
