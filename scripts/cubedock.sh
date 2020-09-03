# Copyright (c) 2020, Gabriel Kim(Doohoon Kim).
# The "CubeDock" is distributed under the "3-clause BSD" license.
# See details COPYING.

# This script was referred at conda.sh in Anaconda.
# see https://github.com/conda/conda/blob/master/conda/shell/etc/profile.d/conda.sh

cubedock() {
    if [ "$#" -ge 1 ]; then
        \local _Command="$1"
        shift

        case "_Command" in
            *)
                CUBEDOCK_INTER_OLDPATH="${PATH}"
                "$CUBEDOCK_EXEC_PATH" "$_Command" "$@"
                #echo "$("$CUBEDOCK_EXEC_PATH" "$_Command" "$@")"
                \local _TerminateSig=$?
                PATH=${CUBEDOCK_INTER_OLDPATH}
                return $_TerminateSig
                ;;
        esac
    fi
}

_cubedock_main() {
    if [ -z "${CUBEDOCK_SHLVL+x}" ]; then
        \export CUBEDOCK_SHLVL=0

        PATH="$(\dirname "$CUBEDOCK_EXEC_PATH")${PATH:+":${PATH}"}"
        \export PATH
    fi
}

_cubedock_main