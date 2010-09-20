# lalsuite_build.m4 - top level build macros
#
# serial 7

AC_DEFUN([LALSUITE_ENABLE_MODULE],[
AM_CONDITIONAL([$1],[test x$$2 = xtrue])
eval $1_ENABLE_VAL="`eval test "$$2" = "true" && echo "ENABLED" || echo "DISABLED"`"
])

AC_DEFUN([LALSUITE_CHECK_LIB],[
m4_pushdef([lowercase],translit([[$1]], [A-Z], [a-z]))
m4_pushdef([uppercase],translit([[$1]], [a-z], [A-Z]))
PKG_CHECK_MODULES(uppercase,[lowercase >= $2],[lowercase="true"],[lowercase="false"])
if test "$lowercase" = "true"; then
  CPPFLAGS="$CPPFLAGS $[]uppercase[]_CFLAGS"
  LIBS="$LIBS $[]uppercase[]_LIBS"
  if test "$LALSUITE_BUILD" = "true"; then
    AC_DEFINE([HAVE_LIB]uppercase,[1],[Define to 1 if you have the $1 library])
    lowercase="true"
  else
    AC_CHECK_LIB(lowercase,[$3],[lowercase="true"],[AC_MSG_ERROR([could not find the $1 library])])
    AC_CHECK_HEADERS([$4],,[AC_MSG_ERROR([could not find the $4 header])])
    if test "$1" != "LALSupport"; then
      LALSUITE_HEADER_LIBRARY_MISMATCH_CHECK([$1])
    fi
    AC_DEFINE([HAVE_LIB]uppercase,[1],[Define to 1 if you have the $1 library])
  fi
else
  AC_MSG_ERROR([could not find the $1 library])
fi
LALSUITE_ENABLE_MODULE(uppercase,lowercase)
m4_popdef([lowercase])
m4_popdef([uppercase])
])

AC_DEFUN([LALSUITE_CHECK_OPT_LIB],[
m4_pushdef([lowercase],translit([[$1]], [A-Z], [a-z]))
m4_pushdef([uppercase],translit([[$1]], [a-z], [A-Z]))
if test "$lowercase" = "true"; then
  PKG_CHECK_MODULES(uppercase,[lowercase >= $2],[lowercase="true"],[lowercase="false"])
  if test "$lowercase" = "true"; then
    if test "$LALSUITE_BUILD" = "true"; then
      AC_DEFINE([HAVE_LIB]uppercase,[1],[Define to 1 if you have the $1 library])
      lowercase="true"
      CPPFLAGS="$CPPFLAGS $[]uppercase[]_CFLAGS"
      LIBS="$LIBS $[]uppercase[]_LIBS"
    else
      CPPFLAGS="$CPPFLAGS $[]uppercase[]_CFLAGS"
      LIBS="$LIBS $[]uppercase[]_LIBS"
      AC_CHECK_LIB(lowercase,[$3],[lowercase="true"],[lowercase=false
        AC_MSG_WARN([could not find the $1 library])])
      if test "$lowercase" = true; then
        AC_CHECK_HEADERS([$4],,[lowercase=false])
        if test "$lowercase" = true; then
          if test "$1" != "LALSupport"; then
            LALSUITE_HEADER_LIBRARY_MISMATCH_CHECK([$1])
          fi
          if test "$lowercase" = true; then
            AC_DEFINE([HAVE_LIB]uppercase,[1],[Define to 1 if you have the $1 library])
          fi
        fi
      fi
    fi
  fi
fi
LALSUITE_ENABLE_MODULE(uppercase,lowercase)
m4_popdef([lowercase])
m4_popdef([uppercase])
])

AC_DEFUN([LALSUITE_HEADER_LIBRARY_MISMATCH_CHECK],[
AC_MSG_CHECKING([whether $1 headers match the library])
lib_structure=`echo $1 | sed 's/LAL/lal/'`VCSInfo
header_structure=`echo $1 | sed 's/LAL/lal/'`HeaderVCSInfo
AC_RUN_IFELSE(
  [AC_LANG_SOURCE([[
#include <string.h>
#include <stdlib.h>
#include <lal/$1VCSInfo.h>
int main(void) { exit(XLALVCSInfoCompare(&$lib_structure, &$header_structure) ? 1 : 0); }
  ]])],
  [
    AC_MSG_RESULT(yes)
  ],
  [
    AC_MSG_RESULT(no)
    AC_MSG_ERROR([Your $1 headers do not match your
library. Check config.log for details.
])
  ],
  [
    AC_MSG_WARN([cross compiling: not checking])
  ]
)
])

AC_DEFUN([LALSUITE_ENABLE_NIGHTLY],
[AC_ARG_ENABLE(
  [nightly],
  AC_HELP_STRING([--enable-nightly],[nightly build [default=no]]),
  [ case "${enableval}" in
      yes) NIGHTLY_VERSION=`date +"%Y%m%d"`
           VERSION="${VERSION}.${NIGHTLY_VERSION}" ;;
      no) NIGHTLY_VERSION="";;
      *) NIGHTLY_VERSION="${enableval}"
         VERSION="${VERSION}.${NIGHTLY_VERSION}" ;;
      esac ],
  [ NIGHTLY_VERSION="" ] )
  AC_SUBST(NIGHTLY_VERSION)
])

AC_DEFUN([LALSUITE_ENABLE_LALFRAME],
[AC_ARG_ENABLE(
  [lalframe],
  AC_HELP_STRING([--enable-lalframe],[compile code that requires lalframe library [default=yes]]),
  [ case "${enableval}" in
      yes) lalframe=true;;
      no) lalframe=false;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-frame) ;;
    esac
  ], [ lalframe=true ] )
if test "$frame" = "false"; then
  lalframe=false
fi
])

AC_DEFUN([LALSUITE_ENABLE_LALMETAIO],
[AC_ARG_ENABLE(
  [lalmetaio],
  AC_HELP_STRING([--enable-lalmetaio],[compile code that requires lalmetaio library [default=yes]]),
  [ case "${enableval}" in
      yes) lalmetaio=true;;
      no) lalmetaio=false;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-metaio) ;;
    esac
  ], [ lalmetaio=true ] )
if test "$metaio" = "false"; then
  lalmetaio=false
fi
])

AC_DEFUN([LALSUITE_ENABLE_LALBURST],
[AC_ARG_ENABLE(
  [lalburst],
  AC_HELP_STRING([--enable-lalburst],[compile code that requires lalburst library [default=yes]]),
  [ case "${enableval}" in
      yes) lalburst=true;;
      no) lalburst=false;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-burst) ;;
    esac
  ], [ lalburst=true ] )
if test "$lalmetaio" = "false"; then
  lalburst=false
fi])

AC_DEFUN([LALSUITE_ENABLE_LALINSPIRAL],
[AC_ARG_ENABLE(
  [lalinspiral],
  AC_HELP_STRING([--enable-lalinspiral],[compile code that requires lalinspiral library [default=yes]]),
  [ case "${enableval}" in
      yes) lalinspiral=true;;
      no) lalinspiral=false;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-inspiral) ;;
    esac
  ], [ lalinspiral=true ] )
if test "$lalmetaio" = "false"; then
  lalinspiral=false
fi
])

AC_DEFUN([LALSUITE_ENABLE_LALPULSAR],
[AC_ARG_ENABLE(
  [lalpulsar],
  AC_HELP_STRING([--enable-lalpulsar],[compile code that requires lalpulsar library [default=yes]]),
  [ case "${enableval}" in
      yes) lalpulsar=true;;
      no) lalpulsar=false;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-lalpulsar) ;;
    esac
  ], [ lalpulsar=true ] )
])

AC_DEFUN([LALSUITE_ENABLE_LALSTOCHASTIC],
[AC_ARG_ENABLE(
  [lalstochastic],
  AC_HELP_STRING([--enable-lalstochastic],[compile code that requires lalstochastic library [default=yes]]),
  [ case "${enableval}" in
      yes) lalstochastic=true;;
      no) lalstochastic=false;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-stochastic) ;;
    esac
  ], [ lalstochastic=true ] )
if test "$lalmetaio" = "false"; then
  lalstochastic=false
fi
])

AC_DEFUN([LALSUITE_ENABLE_LALXML],
[AC_ARG_ENABLE(
  [lalxml],
  AC_HELP_STRING([--enable-lalxml],[compile code that requires lalxml library [default=no]]),
  [ case "${enableval}" in
      yes) lalxml=true;;
      no) lalxml=false;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-lalxml) ;;
    esac
  ], [ lalxml=false ] )
if test "$lalpulsar" = "false"; then
  lalxml=false
fi
])

AC_DEFUN([LALSUITE_ENABLE_BOINC],
[AC_ARG_ENABLE(
  [boinc],
  AC_HELP_STRING([--enable-boinc],[enable BOINC support [default=no]]),
  [ case "${enableval}" in
      yes) boinc=true;;
      no) boinc=false;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-boinc);;
    esac
  ], [ boinc=false ] )
AC_ARG_VAR([BOINC_PREFIX],[BOINC installation directory (optional)])
])

AC_DEFUN([LALSUITE_CHECK_BOINC],
[AC_MSG_CHECKING([whether LAL has been compiled with BOINC support])
AC_TRY_RUN([
#include <lal/LALConfig.h>
#ifdef LAL_BOINC_ENABLED
int main( void ) { return 0; }
#else
int main( void ) { return 1; }
#endif
],
AC_MSG_RESULT([yes])
[boinc=true],
AC_MSG_RESULT([no])
[boinc=false],
AC_MSG_RESULT([unknown])
[boinc=false])
])