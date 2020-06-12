# Auto Estimate

## How to use
- `git clone https://github.com/qicaisheng/auto_estimate.git`
- `cd auto_estimate`
- `sh start.sh`
- input question name
![image info](./docs/img/how-to-use1.png)
- input git repo url
![image info](./docs/img/how-to-use2.png)
- see the report and score
![image info](./docs/img/score.png)

## How to config
![image info](./docs/img/how-to-config.png)


## Dependencies
- Detected code must be java language
- Detected code must config JaCoCo plugin
    - build.gradle
        ```
        plugins {
            id 'jacoco'
        }
        
        jacocoTestReport {
            reports {
                xml.enabled true
            }
        }
        ```
    - pom.xml
        ```
        <build>
            <plugins>
                <plugin>
                    <groupId>org.jacoco</groupId>
                    <artifactId>jacoco-maven-plugin</artifactId>
                    <version>0.8.2</version>
                    <executions>
                        <execution>
                            <goals>
                                <goal>prepare-agent</goal>
                            </goals>
                        </execution>
                        <!-- attached to Maven test phase -->
                        <execution>
                            <id>report</id>
                            <phase>test</phase>
                            <goals>
                                <goal>report</goal>
                            </goals>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
        ```