#!/bin/bash

yarn jar $MYRIA_HOME/build/libs/myria-0.1-all.jar edu.washington.escience.myria.daemon.MyriaDriverLauncher -runtimeClass org.apache.reef.runtime.yarn.client.YarnClientConfiguration -configPath $MYRIA_HOME/myriadeploy -javaLibPath $MYRIA_HOME/build/libs -nativeLibPath $MYRIA_HOME/lib -pythonLibPath $MYRIA_HOME/python
