import requests


def main():
    print('### CONSULTA CEP ###')

    cep_input = input('Digite o CEP para a consulta:')

    if len(cep_input) != 8:
        print('Quantidade de digitos inválida!')
        exit()

    request = requests.get(
        'https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('########## CEP encontrado #########')
        print('CEP: {}'.format(address_data['cep']))
        print('logradouro: {}'.format(address_data['logradouro']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))

    else:
        print(f'{cep_input}: CEP invalido')


option = int(input('Deseja realizar uma nova consulta? \n1.Sim\n 2.Sair'))
if option == 1:
    main()
else:
    print('Saindo...')


if __name__ == '__main__':
    main()
