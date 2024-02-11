# Ulauncher Bitbucket Search Plugin

- This plugin to [Ulauncher](https://ulauncher.io/) allows for faster access of repositories in a Bitbucket workspace without the need to use the search in the web interface.

## Installation

- Install [Ulauncher](https://ulauncher.io/#Download) in your device.
- After starting it, right-click in the "Ulauncher" icon in your system tray and then go to "Preferences".
- In the modal that will open, go to the "EXTENSIONS" tab.
- Click in "Add extension".
- Paste this repository URL: `https://github.com/rsilvr/ulauncher-bitbucket-search` and then click on "Add".

## Setup

- The plugin uses Bitbucket app password in your personal account in order to search for repositories that you have access in a specific workspace. Besides creating an app password, you will also have to inform your workspace id and username.

### Bitbucket App Password

- To create an app password, follow this [guide](https://support.atlassian.com/bitbucket-cloud/docs/create-an-app-password/). Select only the "Repositories" > "Read" permission (it will be enough for what this extension does).

### Bitbucket username

- To find out your username, log into your Bitbucket account and in any page select the Settings cog in the upper-right corner of the top navigation bar. Under "Personal settings", select "Personal Bitbucket settings".
- Then scroll to "Bitbucket profile settings" section and copy the "Username".

### Bitbucket workspace

> A workspace is where you will create repositories, collaborate on your code, and organize different streams of work in your Bitbucket Cloud account.

- To find out the workspace id you are working on, go to any repository page and then copy this part of the URL: www[]().bitbucket.org/**workspace ID**/my-repository-name

### Putting all together

- To set these credentials into the plugin, right-click in the "Ulauncher" icon in your system tray and then go to "Preferences".
- In the modal that will open, go to the "EXTENSIONS" tab.
- Look for "Bitbucket Search".
- There fill down "Bitbucket Workspace", "Bitbucket Username" and "Bitbucket App Password" and then click in the "Save" button.

## Usage

- After this setup, you can start searching:
  - First, type the extension keyword "bbt" (you can change this in the extension preference if you want).
  - Then you can type any term from the repository name or [slug](https://confluence.atlassian.com/bbkb/what-is-a-repository-slug-1168845069.html).
  - Select a result and then press Enter.
  - The extension will show you some options, each one a shortcut to the repository:
    - The "Source" page, where you can access the main branch code. It is also the repository homepage.
    - The "Pull-Requests" page, where you can access the repo pull-requests list.
    - The "Pipelines" page, where you can access the pipelines executions list.
    - The "Settings" page, where you can change the repository configurations.
