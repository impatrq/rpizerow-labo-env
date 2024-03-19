# GitHub CLI

Estas son algunas instrucciones para poder pushear a un repo personal desde la RPiZeroW.

Vamos a usar [GitHub CLI](https://cli.github.com/) para facilitar el problema de la autenticacion de credenciales. Este programa ya esta instalado en todas las placas de desarrollo, puede verificarse escribiendo:

``` bash
gh --version
```

Y debemos ver que no hay error en cuanto al comando.

Para poder usarlo, vamos a necesitar crear un token de acceso personal en GitHub para que al pushear nuestros cambios a un repositorio personal, GitHub pueda acreditar nuestra identidad. Esto puede hacerse desde la configuracion en nuestro perfil de GitHub, dentro de la seccion de configuracion de desarrollador. Informacion mas detallada pueden encontrarla en este [link](https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Al crear el token, tendremos que darle ciertos alcances. GitHub CLI nos va a pedir que los alcances minimos sean: `repo`, `read:org` y `workflow`.

Para poder usar GitHub CLI escribimos en el bash:

```bash
gh auth login
```

Esto nos va a solicitar algunos datos:

- A que tipo de cuenta loguearse? GitHub.com
- Protocolo preferido? HTTPS
- Autenticar Git con credenciales de GitHub? Si
- Como autenticar GitHub CLI? Con token, vamos a pegar el que generamos cuando lo solicite.

Una vez logueados, vamos a poder pushear nuestros cambios a repositorios personales sin inconvenientes. Cuando estemos listos para salir de la RPiZeroW, vamos a desloguearnos con:

```bash
gh auth logout
```
