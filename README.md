# M2Dev Client

This repository contains all client-side data, including locale files, configurations, and descriptive text used by the game client.

**For installation and configuration, see [instructions](#installationconfiguration) below.**

## 📋 Changelog

### ⬆️ Feature Improvements
* **Snow mountain and Snow Dungeon updated:** Updated Snow mountain and Snow Dungeon terrain, environment and textures
* **Protos updated:** Updated protos for all locales with the new items and mobs/NPCs for the Snow Dungeon (some translations may be incomplete)
* **Item icons and descriptions updated:** Updated item icons and descriptions for new items for all locales (some translations may be incomplete)

<br>
<br>

---

<br>
<br>

# Installation/Configuration
This is the final part of the entire project and it's now time to pack everything up for your first launch of the game!

Below you will find a comprehensive guide on how to configure all the necessary components from scratch.

This guide is made using a **Windows** environment as the main environment and **cannot work in non-Windows operating systems!** If you haven't yet setup your Server or haven't built the Client Source, **now is the chance to do so as these are required steps to continue!**

This guide also uses the latest versions for all software demonstrated as of its creation date at February 4, 2026.

© All copyrights reserved to the owners/developers of any third party software demonstrated in this guide other than this project/group of projects.

<br>

### 📋 Order of projects configuration
If one or more of the previous items is not yet configured please come back to this section after you complete their configuration steps.

>  - ✅ [M2Dev Server Source](https://github.com/d1str4ught/m2dev-server-src)
>  - ✅ [M2Dev Server](https://github.com/d1str4ught/m2dev-server)
>  - ✅ [M2Dev Client Source](https://github.com/d1str4ught/m2dev-client-src)
>  - ▶️ [M2Dev Client](https://github.com/d1str4ught/m2dev-client)&nbsp;&nbsp;&nbsp;&nbsp;[**YOU ARE HERE**]&nbsp;&nbsp;&nbsp;&nbsp;[**ALSO CONTAINS ADDITIONAL INFORMATION FOR POST-INSTALLATION STEPS**]

<br>

### 🧱 Software Prerequisites

<details>
  <summary>
    Please make sure that you have installed the following software in your machine before continuing:
  </summary>

  <br>

  > <br>
  >
  >  - ![Python](https://metin2.download/picture/PQiBu5Na1ld90rixm0tVgstMxR43OpIn/.png)&nbsp;&nbsp;**Python**:&nbsp;&nbsp;The software used to execute python scripts. It is **recommended to ADD TO PATH** at the end of the installation. [Download](https://www.python.org/downloads/)
  >
  > <br>
  >

</details>

<br>

### ⬇️ Obtaining the Client

To clone the client, open up your command prompt and `cd` into your desired location or create a new folder wherever you want and download the project using `Git`.

<details>
  <summary>
    Here's how
  </summary>

  <br>

  >
  > <br>
  >
  >
  > Open up your terminal inside or `cd` into your desired folder and type this command:
  >
  > ```
  > git clone https://github.com/d1str4ught/m2dev-client.git
  > ```
  >
  > <br>
  >
  > ### ✅ You have successfully obtained the Client project!
  >
  > <br>
  >
</details>

<br>

### 📦 Packing up the protos

Before packing everything else, we make sure that our `item_proto` and `mob_proto` files are packed with the latest updates from the server.

<details>
  <summary>
    Instructions
  </summary>

  <br>

  >
  > <br>
  >
  >
  > Go inside the **build** folder of your **Client Source** cloned repository. There, you should have a **bin** folder and inside that, you should have a **Debug**, **Release**, **RelWithDebInfo** or **MinSizeRel** folder, depending on your build configuration selection.
  >
  > In that folder you should be seeing all your binaries:
  >
  > ![](https://metin2.download/picture/4cVxiU2Ac8CON58Gh70f6Do34dGBXpOz/.png)
  >
  > There you should be seeing the **DumpProto.exe**, the tool you will use to compile the protos. You can leave it there or move it to a new, clean location to work.
  >
  > Either you are running your Server project on Windows or FreeBSD, go to `share/conf` and paste all the required files to compile your protos.
  >
  > To compile `item_proto`, paste:
  > - `item_proto.txt`
  > - At least one `item_names_<XX>.txt` or `item_names.txt` (where `XX` = locale name)
  >
  > To compile `mob_proto`, paste:
  > - `mob_proto.txt`
  > - At least one `mob_names_<XX>.txt` or `mob_names.txt` (where `XX` = locale name)
  >
  > <br>
  >
  > Compilation of `item_proto` is independent of `mob_proto`.
  >
  > **DumpProto.exe** will compile all protos found in its current directory.
  >
  > **You can paste multple `item_names<XX>.txt`/`mob_names_<XX>.txt` at one go if you wish to!**
  >
  > <br>
  >
  > The following example will be showing the compilation of all protos for all locales in one go.
  >
  > Paste everything **in the same directory as DumpProto.exe**:
  >
  > ![](https://metin2.download/picture/IkVBPAt0NF6TLk2YhDZM9aNJ2Y0H8cWy/.png)
  >
  > <br>
  >
  > Double click **DumpProto.exe** and wait for the compiling to finish. This may take a while depending on how many `item_names` or/and `mob_names` exist in the folder and from the Build Configuration you selected in Visual Studio (`Debug`, `Release`, etc...)
  >
  > After compiling is done, **DumpProto.exe** will automatically close and you should be seeing the following in your **DumpProto.exe** folder:
  >
  > - If you had `item_proto.txt` + `item_names.txt`, a new `item_proto` file
  > - If you had `mob_proto.txt` + `mob_names.txt`, a new `mob_proto` file
  > - For every `item_names_<XX>.txt`, a `locale/XX` folder with `item_proto` inside it
  > - For every `mob_names_<XX>.txt`, a `locale/XX` folder with `mob_proto` inside it
  >
  > ![](https://metin2.download/picture/lSX57AgRuldiQ5v02m8i2v0Y3qMeEq6Y/.png)
  >
  > ![](https://metin2.download/picture/16abaf06b4MiMt1ofAMNtdPms3l7tHmZ/.png)
  >
  > **Non-localized protos**
  >
  > These are your **default locale's protos**. If your server for example is configured to **English** (`share/locale/english`), your `item_proto`/`mob_proto` would be the English translation, and in that case, `locale/en` would be missing from the new `locale` folder inside the **DumpProto.exe**.
  >
  > **Copy the new protos in the assets folder**
  >
  > In your client's `assets/locale` folder, every locale must have its `item_proto` and `mob_proto` to work. Paste all the new protos you created in there. You can also copy the `locale` folder created from **DumpProto.exe** and paste it directly into the `assets/locale` folder, then if prompted, select to replace the existing files.
  >
  > If you compiled protos for your **default server locale**, you must paste the manually in their locale folder as well (e.g., `assets/locale/locale/en` for English protos).
  >
  > <br>
  >
  > ### ✅ You have successfully compiled the item/mob proto files and distributed them to their respective directories!
  >
  > <br>
  >
</details>

<br>

### 📦 Packing up the client assets and configuring the IP

Now that you have your proto files, it's time for the few final steps.

<details>
  <summary>
    The few final steps
  </summary>

  <br>

  >
  > <br>
  >
  >
  > In the `assets/root` folder, find a file called `serverinfo.py` and open it with an editor of your choice. In the `SERVER_IP` variable, replace the value with:
  > - **FreeBSD Servers**: Your IP from `ifconfig`
  > - **Windows Servers**: `127.0.0.1`, `localhost`, or your IP (**Preferred**) from the command `ipconfig /all`, it's all the same thing
  >
  > ![](https://metin2.download/picture/fECU7Apak7OiL1yj1jSh5B1I3O72xSvm/.png)
  >
  > Save the file and go back to your command prompt.
  >
  > <br>
  >
  > Now `cd` in the `assets` folder if not already there and execute the `PackMaker.exe` with the help of the `pack.py` script that is included in the `assets` folder:
  >
  > ```
  > python pack.py --all
  > ```
  >
  > This process will take some time, grab a coffee and come back in a little bit.
  >
  > After it's done, you won't see any messages, but if the command prompt is ready for the next command, you're done!
  >
  > ![](https://metin2.download/picture/pSAwVDRpqgiu49T7GrXNDH4Voyd6LpGD/.png)
  >
  > **Note**: `--all` packs everything inside the `assets` folder, if you wanna pack only one folder (`root` for example), you can execute this command instead:
  > 
  > ```
  > python pack.py root
  > ```
  >
  > <br>
  >
  > ### ✅ You have successfully packed the assets folders!
  >
  > <br>
  >
</details>

<br>

## 🎉 Launching the game
With your Server running, go to the root folder of the Client project and execute your compiled `Metin2_XX.exe` launcher.

You know how it goes from here.

Available accounts:
 - admin
 - test

Password for both is **123456789**

**🤩 Your client is now fully built and packed!**

![](https://metin2.download/picture/jD6AhAORtm6wpJx1uD1NcTRv1crpT2nv/.png)

<br>
<br>

## 🔥 All systems check, the guide is complete!

<br>
<br>

## Recap
After finishing this part, you should now have knowledge of:

 - Compiling client protos from server `txt` files
 - Packing the `asset` folders

---

<br>
<br>

## Next steps
These are some next steps that apply to all project, regardless of the operating system you use.

### 💅 Maintaining the repositories (cross-platform)

These next steps can be done in both Windows and FreeBSD environments.

<details>
  <summary>
    How to keep your repos up to date
  </summary>

  <br>

  >
  > <br>
  >
  > To update your repositories when a new version comes out, open up a terminal or go to the root folder of the desired project (let's take the **Server Source** for example).
  >
  > **Type these commands (in every project that requires updates):**
  >
  > Making sure that you are in the main branch
  >
  > ```
  > git checkout main
  > ```
  > If you get the message "Your branch is up to date with 'origin/main'." at the end, you have no updates available.
  >
  > Checking remote status
  >
  > ```
  > git remote -v
  > ```
  >
  > You should be seeing "**origin**" twice. If you have cloned the repo from your custom fork you should also be seeing "**upstream**" (more below).
  >
  > Getting the updates
  > ```
  > git fetch origin
  > ```
  >
  > Merging the updates
  >
  > ```
  > git merge origin/main
  > ```
  >
  > <br>
  >
  > ### ✅ You have successfully updated your repository!
  >
  > <br>
  >
</details>

<br>

### 🎟️ Opening a Github issue
This is the best and maybe one of the fastest ways for the maintainer(s) of the project to see what's wrong.

<details>
  <summary>
    How to submit an Issue
  </summary>

  <br>

  >
  > <br>
  >
  > Create an account for Github if you haven't already and fo to the problematic project's page (e.g., **Client**). Go to **Issues** at the top left corner.
  >
  > ![](https://metin2.download/picture/qdS797F8r9f82MOHmJ6GJHjZnhHp8u75/.png)
  >
  > Click on the green button that says "**New issue**".
  >
  > ![](https://metin2.download/picture/z501GwVm5g6B45YdZPAUhVBu7iGXGC9G/.png)
  > There describe your issue:
  >
  > ![](https://metin2.download/picture/2Ylll9Gj2p53PpEYMkf3AWDnmNSQ5nHV/.png)
  >
  > When the devs/maintainers see your issue, they will probably start fixing it (depends on how serious of a bug it is and how detailed your explanation was).
  >
  > People don't like to waste their time or other people's time, the best your description is, the more likely it is for someone to show interest and the less chance you have to get a "What do you mean?" question and wait another 24 hours for someone to understand the issue.
  >
  > <br>
  >
  > ### ✅ You have successfully complained to the manager! Way to go Karen!
  >
  > <br>
  >
</details>

<br>

### ⭐ Creating a PR
Feeling ready to take on the WORLD??? Start by your first pull request!

<details>
  <summary>
    The first step in becoming a legend
  </summary>

  <br>

  >
  > <br>
  >
  > Ok, so you've played with the files and the source, you had a nice idea and you developed it. You have now anxiety depression from too much trial and error, your mortgage is 3 months behind, and you may have cried a little, but **it's done**! You **TESTED THOUROUHLY**, **again and again**, then woke up in the middle of the night to test ONE MORE TIME and you liked what you saw. You are ready for your first contribution to the project! 😂
  >
  > Here is an example on how to PR using the **Server Source** as an example.
  >
  > First you need to fork the official project as a project of your own, an identical copy that you own, tied to the original one:
  >
  > ![](https://metin2.download/picture/WXBXPF9seW2nzcsDTG1bjrjjE6D7P6BN/.png)
  >
  > Accept the defaults and finish the fork creation.
  >
  > <br>
  >
  > You now have the project in your repositories!
  >
  > ![](https://metin2.download/picture/b3kBjNik0n5a2osi92cnQtbUs7SCwS03/.png)
  >
  > <br>
  >
  > As you can see it says "**forked from d1str4ught/m2dev-server-src**".
  >
  > Also the highlighted message means that there are no pending changes in the official repo that this fork is lacking, nor it has any changes that the upstream (official) repo doesn't have. This is the state your fork needs to be in order to push a PR!
  >
  > <br>
  >
  > Next, you must download **YOUR FORK**. The upstream (official project) is **not** your fork and you cannot push a PR to it because it is not owned by you.
  >
  > Go to your terminal and clone your fork:
  >
  > ![](https://metin2.download/picture/5AojCE2vcNVr4eFCxDEDQRWmQBMl9WZ0/.png)
  >
  > Obviously type your own Github username in the URL.
  >
  > <br>
  >
  > Now add an upstream. An upstream is a repo that your fork gets updates from and is checked against whenever you are looking for changes. Execute this command:
  >
  > ```
  > git remote add upstream https://github.com/d1str4ught/m2dev-server-src.git
  > ```
  >
  > This time, use the link from the official project as the upstream.
  >
  > Verify with
  >
  > ```
  > git remote -v
  > ```
  >
  > ![](https://metin2.download/picture/7inn7Ej1lqSNbVer28Z305x7q75c16Zj/.png)
  >
  > As you can see now we have 2 origins (your profile's URLs) and 2 upstreams.
  >
  > <br>
  >
  > Here is how to check for changes (very similar to the commands we saw earlier about updating the repos):
  >
  > **WARNING: This will overwrite all your modified files! Make sure they are copied in a safe place first!**
  >
  > ```
  > git fetch upstream
  > git merge upstream/main
  > git clean -fd
  > ```
  >
  > That's it, simply replace `origin` with `upstream` and you are now updating your cloned fork with the official repo's latest updates.
  >
  > **But these changes are only local.** It is very important to update your fork in Github before pushing a PR. If you have ran all these commands, do the following:
  >
  > ```
  > git checkout main
  > git push origin main
  > ```
  > Once this last one is done, any `X commits behind` in your forked repo's page on Github should be gone and your fork should be updated to the latest version as the original project. You have basically made it a perfect copy.
  >
  > <br>
  >
  > You are now ready to PR your changes.
  >
  > Copy all the modified files into the updated project clone folder at the right places.
  >
  > <br>
  >
  > Now it is recommended to create a new branch for your PR to keep things organized and to have online backups in case something goes wrong.
  >
  > Branches are different versions of the repository, the `main` is the default one and it is recommended to be always kept "clean".
  >
  > ![](https://metin2.download/picture/TM3ZrpPcJpQ1nnPEzd0vs9QBIutbYyjM/.png)
  >
  > After you have copied your modified files, go to the root folder of the project in your local machine and type these commands in the terminal:
  >
  > ```
  > git checkout -b new_branch_name
  > git add .
  > git commit -m "Fixed the pancake bug, added translations for dungeon X"
  > git push -u origin new_branch_name
  > ```
  >
  > You may need to login with your Github account in your terminal for pushing. If your password doesn't work:
  >
  > - Go to the Developer settings in the Github website
  > - Go to Access tokens and create a new Classic token for general use
  > - Select the `repo` scope and name they token.
  > - Once you create it, copy the code in the green box, you won't have another chance to copy it
  > - Paste that code as your password in the terminal
  >
  > Once your push is complete, you should be seeing your new branch in the forked repo page!
  >
  > ![](https://metin2.download/picture/wEyPQVmLjkA6eEwpSCRPBjzi0AfQikiv/.png)
  >
  > Click the **Compare & pull request** green button in order to submit your new updates as a PR.
  >
  > ![](https://metin2.download/picture/NZaLoylP4oc415FTO56cOhb9i63yPr2O/.png)
  >
  > <br>
  > 
  > `Able to merge` with green font is good. Add a title if you don't have one already and click the green **Create pull request** at the bottom.
  >
  > <br>
  >
  > ### ✅ You just submitted your first PR!
  >
  > <br>
  >
</details>

You should now have full knowledge of how to get started with your project and if you wish to, give back to the community!

<br>

## 🔥 You are now an M2Dev Master!
Can't wait to see what you'll create!

<br>
<br>

---

<br>
<br>

## Recap
After finishing this part, you should now have knowledge of:

 - Updating your repos
 - Forking your own copies of the repos
 - Opening issues in Github
 - Submitting PRs after you successfully update the code

---

<br>
<br>

## A huge shoutout
To the entire community that's been supporting this project and makes things possible!

⭐ **NEW**: We are now on Discord, feel free to [check us out](https://discord.gg/ETnBChu2Ca)!