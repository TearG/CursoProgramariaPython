import sys

preco_cenoura = 4.5 #sim
preco_oleo = 12 #sim
preco_fermento = 15 #sim
preco_leite = 5 #nao
preco_acucar = 6 #sim
preco_ovos = 12 #sim

def soma_ingrediente(tem_cenoura, tem_acucar, tem_ovos, tem_oleo, tem_fermento, tem_leite):
	total_compra = 0
	if tem_cenoura:
		total_compra = total_compra + preco_cenoura
	if tem_acucar:
		total_compra = total_compra + preco_acucar
	if tem_ovos:
		total_compra = total_compra + preco_ovos
	if tem_oleo:
		total_compra = total_compra + preco_oleo
	if tem_fermento:
		total_compra = total_compra + preco_fermento
	if tem_leite:
		total_compra = total_compra + preco_leite
	return total_compra

if __name__ == "__main__":

	terminal_tem_cenoura = sys.argv[1] == "Sim"
	terminal_tem_acucar = sys.argv[2] == "Sim"
	terminal_tem_ovos = sys.argv[3] == "Sim"
	terminal_tem_oleo = sys.argv[4] == "Sim"
	terminal_tem_fermento = sys.argv[5] == "Sim"
	terminal_tem_leite = sys.argv[6] == "Sim"

	total = soma_ingrediente(terminal_tem_cenoura, terminal_tem_acucar, terminal_tem_ovos, terminal_tem_oleo, terminal_tem_fermento, terminal_tem_leite)

	print("Total dos Ingredientes: ", total)