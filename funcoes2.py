def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

loginUsuario('admin')
loginUsuario('Admin')
loginUsuario('User')
loginUsuario('usuário')
