_jq() {
    [[ -z $(type -P jq) ]] && return 1

    local json=${SHEET_FILE:-~/.tt-sheet.json}
    jq -r '[.[][].'"$1"' | select(. != null)] | flatten | unique | @tsv' ${json} 2>/dev/null
}

_tt() {
    [[ -z $(type -P tt) ]] && return 1

    local sub cur prv
    sub=${COMP_WORDS[1]}
    cur=${COMP_WORDS[COMP_CWORD]}
    prv=${COMP_WORDS[COMP_CWORD-1]}

    local -a subcmds
    subcmds=(help start stop note ect tag edit csv status report log calview)

    local -a projects tags
    projects=($(_jq name))
    tags=($(_jq tags))

    case ${COMP_CWORD} in
        1)
            COMPREPLY=($(compgen -W "${subcmds[*]}" -- ${cur}))
            ;;
        2)
            case ${prv} in
                start|report)
                    COMPREPLY=($(compgen -W "${projects[*]}" -- ${cur}))
                    ;;
                stop)
                    COMPREPLY=($(compgen -W "now $(date '+%H:%M')" -- ${cur}))
                    ;;
                tag)
                    COMPREPLY=($(compgen -W "${tags[*]}" -- ${cur}))
                    ;;
                csv|status)
                    COMPREPLY=($(compgen -W "--no-color" -- ${cur}))
                    ;;
                log)
                    COMPREPLY=($(compgen -W "$(date -d today '+%Y-%m-%d')" -- ${cur}))
                    ;;
                calview)
                    COMPREPLY=($(compgen -W "$(date '+%m')" -- ${cur}))
                    ;;
            esac
            ;;
        3)
            case ${sub} in
                start)
                    COMPREPLY=($(compgen -W "now $(date '+%H:%M')" -- ${cur}))
                    ;;
                report)
                    COMPREPLY=($(compgen -W "--no-color" -- ${cur}))
                    ;;
                log)
                    COMPREPLY=($(compgen -W "$(date '+%Y-%m-%dT%T')" -- ${cur}))
                    ;;
                calview)
                    COMPREPLY=($(compgen -W "$(date '+%Y') --no-color" -- ${cur}))
                    ;;
            esac
            ;;
        *)
            COMPREPLY=()
            ;;
    esac
}

complete -o nosort -F _tt tt
