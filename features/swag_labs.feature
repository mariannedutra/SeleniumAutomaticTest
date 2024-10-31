# language: pt
Funcionalidade: Finalização de compra no SauceDemo
    Como um usuário
    Quero fazer login, adicionar um item ao carrinho e finalizar a compra

Cenário: Realizar uma compra com o usuário performance_glitch_user
    Dado que o usuário acessa a página de login do SauceDemo
    Quando o usuário faz login com o nome de usuário "performance_glitch_user" e a senha "secret_sauce"
    E o usuário adiciona "Sauce Labs Fleece Jacket" ao carrinho
    E o usuário vai para o carrinho
    E o usuário inicia o processo de checkout
    E o usuário preenche as informações de checkout com nome "Carlos", sobrenome "Silva" e CEP "12345"
    E o usuário finaliza o pedido
    Então a página de confirmação de pedido deve ser exibida
