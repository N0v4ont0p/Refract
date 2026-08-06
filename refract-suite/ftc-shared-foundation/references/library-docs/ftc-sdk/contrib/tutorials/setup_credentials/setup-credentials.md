> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/contrib/tutorials/setup_credentials/setup-credentials.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Setup Git Credentials
======================
:bdg-danger:`One Time Only` :bdg-warning:`Local`

.. note:: This is a one-time setup that is only necessary for local development. Codespace users may skip this step.

This step enables you to push changes to your forked repository. It is necessary 
in order for GitHub to authenticate you as an authorized user.

1. Install `GitHub CLI <https://cli.github.com/>`_
2. Enter the following command in your terminal to authenticate with GitHub:

   .. code-block:: bash

      gh auth login

3. Follow the prompts to authenticate with GitHub.

.. figure:: images/terminal-auth.png
   :alt: GitHub CLI Authentication
   :align: center
