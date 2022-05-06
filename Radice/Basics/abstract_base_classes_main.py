import abstract_base_classes as template 

sm = template.state_machine()
sm.current_state()

sm.recieve_event(template.lost_money())
sm.current_state()

sm.recieve_event(template.recieved_money())
sm.current_state()

