fertilizer_indices=[0,1]
fertilizers=["ammonium nitrate","tripple superphosphate","calcium ammoinum nitrate"]
amounts=[10,20]
suppliers=['supplier abc','supplier xyz','agribiz suppliers ltd']
prices=[1000,2000,3500]
def predict(crop,area,location):
    fertilizer=fertilizer_indices[crop]
    unit_amount=amounts[fertilizer]
    amount=unit_amount*area
    supplier=suppliers[location]
    raw_price=area*prices[fertilizer]
    return [fertilizer,amount,supplier,raw_price]
def interpreter():
    raw_prediction=predict(1,1000,1)  
    fertilizer=fertilizers[raw_prediction[0]]
    raw_price=raw_prediction[3]
    price='Sh.'+str(raw_price)
    return [fertilizer,raw_prediction[1],raw_prediction[2],price]
print(interpreter())