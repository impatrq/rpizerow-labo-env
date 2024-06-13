# Raspberry Pi Zero W Labo Environment

Contenidos del README:

- [Como empezar](#como-empezar)
- [git add, commit, push](#git-add-commit-y-push)
- [Documentación sobre placa de desarrollo](#documentación-sobre-placa-de-desarrollo)

## Como empezar

1- Si no lo hemos hecho ya, hacer un [fork](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) de este repositorio para que tengamos una copia bajo nuestro usuario. Si ya hicimos un fork previamente, asegurémonos de que el fork esté [sincronizado](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) con el respositorio original. 

2- Asegurarse de que la computadora desde donde se van a conectar esté en la **Red Alumnos**.

3- Iniciar sesion en la RPiZeroW con SSH a traves de Putty, Termius o shell. El usuario y clave son `rpizerow`. En cuanto al hostname o direccion de IP y el puerto, va a depender de la RPiZeroW que queremos usar. Abajo hay una tabla con las posibles combinaciones:

<table>
	<thead>
		<th>RPiZeroW</th>
		<th>Direccion IP</th>
		<th>Puerto</th>
	</thead>
	<tbody>
		<tr>
			<td>rpizerow-01</td>
			<td rowspan=3>192.168.124.113 (consultar)</td>
			<td>2221</td>
		</tr>
		<tr>
			<td>rpizerow-02</td>
			<td>2222</td>
		</tr>
		<tr>
			<td>rpizerow-03</td>
			<td>2223</td>
		</tr>
	</tbody>
</table>

Ejemplo para SSH desde shell:

```bash
ssh rpizerow@192.168.124.113 -p 2221
```

Si usan Putty, se escribe IP y el puerto por separado.

Campo de IP:

```
rpizerow@192.168.124.113
```

Campo de puerto:

```
2221
```

Con esto nos logueamos con el usuario rpizerow en la RPiZeroW 01.

4- Si nunca lo hicimos, crear dentro del home de rpizerow un directorio con nuestro apellido con el comando _mkdir_. Ejemplo:

```bash
mkdir gonzalez
```

Si el directorio ya existe, ir al paso 5.

5- Entrar al directorio, con el comando `cd`. Ejemplo:

```bash
cd gonzalez
```

5- Clonar el fork de este repositorio con el comando a continuación reemplazando _USERNAME_ por el que corresponda.:

```bash
git clone https://github.com/USERNAME/rpizerow-labo-env.git
```

**Nota: si les pide autorización de usuario y contraseña de GitHub, el link al repositorio lo copiaron mal.**

6- Navegar hasta el repositorio con _cd_ y crear un entorno virtual. Sería:

```bash
cd rpizerow-labo-env
```

7- Seguir las instrucciones del README de las actividades que se vayan a hacer.

## git add, commit y push

Una vez que hayamos terminado una actividad o ejercicio, tenemos que hacer los cambios en el repositorio con git para poder sincronizarlos. La lógica siempre es `git add`, `git commit`, `git push`.

Cuando tenemos algún archivo nuevo o modificado, lo primero es agregarlo a git para que trackee los cambios:

```bash
git add archivo
```

Pueden revisar los archivos que tienen que agregar con el comando:

```bash
git status
```

Luego, vamos a tener que especificar quién somos para que quede registrado la persona que está haciendo los cambios en el repositorio con `git config`. Ejemplo:

```bash
git config user.email "gonzalez@impatrq.com" && git config user.name "Gonzalo Gonzalez"
```

Después, tenemos que hacer un commit para registrar el cambio que hicimos y proporcionar un mensaje apropiado con el tipo de cambio según el estándar de [commits convencionales](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines). Ejemplo:

```bash
git commit -m "feat: programa que prende un LED rojo con boton"
```

Cuando hayamos hecho todos los commits, vamos a usar [GitHub CLI](https://cli.github.com/) para facilitar el problema de la autenticacion de credenciales. Este programa ya esta instalado en todas las placas de desarrollo, puede verificarse escribiendo:

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

Una vez logueados, vamos a pushear los cambios con:

```bash
git push
```

Por ultimo, nos deslogueamos de GitHub CLI con:

```bash
gh auth logout
```

## Documentación sobre placa de desarrollo

En la medida que se desarrollen las distintas actividades, va a ser necesario informacion del hardware que estamos usando. Pueden encontrar esquematico, PCB y otros documentos en este [repositorio](https://github.com/impatrq/rpizerow-labo-kit).
